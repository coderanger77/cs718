re archi proj.. set the base line --> 1 hour
    create 3 apps[reporter,admin,resolver]
    models:
   
    bug-->title,description,files,reporter,tags,bugid
    
    reporter->username,paswd,
    
    bug_reporter->bugid,reporter,resolver,starttime,endtime[if status resolved]
    #couldn't add tags and files. do this once the basic is done.


    resolver->name,paswd,role,tags
    
    
    reporter:
    report a bug
    search for bugs [for status of the bugs,link to update, escalate,view report]
    update bugs[description,add files, change status]
    


    admin:
    add resolver /approve registration
    remove/change previliges and users.
    resolver:
    view assigned bugs
