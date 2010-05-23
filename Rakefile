require 'rake/clean'

task :rsync do
    puts 'Rsyncing site...'
    sh "rsync -a _site/ #{ENV['DAVEDASH']}html"
    sh "rsync -a _conf/ #{ENV['DAVEDASH']}conf"
    puts 'Done.'
end

task :deploy do
    puts 'Cleaning _site...'
    CLEAN.include('_site/**')
    rmtree CLEAN
    Rake::Task["cloud"].invoke
    Rake::Task["tag"].invoke
    puts 'Building site...'
    sh 'jekyll'
    Rake::Task["rsync"].reenable
    Rake::Task["rsync"].invoke
end

task :cloud do
    puts 'Generating tag cloud...'
    require 'rubygems'
    require 'jekyll'
    include Jekyll::Filters

    options = Jekyll.configuration({})
    site = Jekyll::Site.new(options)
    site.read_posts('')

    html = ''

    site.tags.sort.each do |tag, posts|

      s = posts.count

      if s == 1 then
        next
      end

      font_size = (Math.log(s)*1.5).round
      class_name = 'size_%d' % font_size
      html << "<li class=\"#{class_name}\">
            <a href=\"/tag/#{tag}/\" title=\"Pages tagged #{tag}\" rel=\"tag\">
            #{tag}</a></li>"
    end

    File.open('_includes/tags.html', 'w+') do |file|
      file.puts html
    end

    puts 'Done.'
  end



desc 'Generate tags page'
task :tags do
  puts "Generating tags..."
  require 'rubygems'
  require 'jekyll'
  include Jekyll::Filters

  options = Jekyll.configuration({})
  site = Jekyll::Site.new(options)
  site.read_posts('')
  site.tags.sort.each do |category, posts|

    next if category == ".net"
    html = ''
    html << <<-HTML
---
layout: default
title: Entries tagged "#{category}"
tag: #{category}
type: "#{category.gsub(/\b\w/){$&.upcase}}"
---
    <h2 id="#{category}">Entries tagged "#{category}"</h2>

    <ol>
      {% for post in site.tags['#{category}'] %}
      {% include item.html %}
      {% endfor %}
    </ol>
    HTML

    FileUtils.mkdir_p "tag/#{category}"
    File.open("tag/#{category}/index.html", 'w+') do |file|
      file.puts html
    end

    # ATOM.xml

    html = ''
    html << <<-HTML
---
layout: nil
---
<?xml version="1.0" encoding="utf-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">

 <title>Dave Dash</title>
 <link href="http://davedash.com/tag/#{category}/atom.xml" rel="self"/>
 <link href="http://davedash.com/tag/#{category}"/>
 <updated>{{ site.time | date_to_xmlschema }}</updated>
 <id>http://davedash.com/</id>
 <author>
   <name>Dave Dash</name>
   <email>dd+atom1@davedash.com</email>
 </author>

 {% for post in site.tags['#{category}'] %}
 <entry>
   <title>{{ post.title }}</title>
   <link href="http://davedash.com{{ post.url }}"/>
   <updated>{{ post.date | date_to_xmlschema }}</updated>
   <id>http://davedash.com{{ post.id }}</id>
   <content type="html">{{ post.content | xml_escape }}</content>
 </entry>
 {% endfor %}

</feed>
    HTML

    File.open("tag/#{category}/atom.xml", 'w+') do |file|
      file.puts html
    end

  end
  puts 'Done.'
end

