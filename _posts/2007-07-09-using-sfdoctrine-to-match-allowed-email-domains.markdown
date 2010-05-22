---
wordpress_id: 106
layout: post
title: Using sfDoctrine to match allowed email domains
wordpress_url: http://spindrop.us/2007/07/09/using-sfdoctrine-to-match-allowed-email-domains/
site: spindrop
tags: [programming, symfony, symfony, php, propel, startups, doctrine, optiopt, validators]
---
[tags]php, propel, doctrine, validators, symfony, optiopt, startup[/tags]

I'm a co-founder at an online finance web site and I'm in charge with building out the site.  Our rollout strategy is to let a a handful of companies at a time, so we're limiting registration based on your company's email address.

I decided to follow the bandwagon and use PHP Doctrine.  We'll define two objects, `Company` and `CompanyDomain`:

	Company:
	  tableName: company
	  columns:
	    name: {type: string(100)}
	    created_at: timestamp
	    updated_at: timestamp
  
	CompanyDomain:
	  tableName: company_domain
	  columns:
	    company_id:
	      foreignClass: Company
	      cascadeDelete: true
	    pattern: {type: string(100)}

Where a `CompanyDomain` represents a domain name for a company.  E.g. Motorola might have both `motorola.com` and `mot.com`.

We can validate a signup form and see if we've got an email address from a domain we recognize.  I like using the `validationXXX` methods in an action class for specific validation.  I made one called `validateSignup`:

	public function validateSignup()
	{
		if ($this->isPost())
		{
			$email = $this->getRequestParameter('company_email');
			if (!$company = CompanyTable::match($email))
			{
				$this->getRequest()->setError('company_email', 'Your work email doesn\'t appear to belong to any of the registered companies.');
		    	return false;
			}
			return true;
		}
	}

In our `CompanyTable` we create a static function `CompanyTable::match`:

	static public function match($email)
	{
		$company = Doctrine_Query::create()->from('Company c, c.CompanyDomains d')->where('? LIKE CONCAT(\'%\', pattern)', $email)->execute()->getFirst();
	
		return $company;
	}

Note that we transparently do a join in the `->from()` statement.  If there's a match we get a company object (which we can associate with the new user) otherwise we get a `null` object.

Enjoy.
