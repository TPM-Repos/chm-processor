Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ApplicationPluginLoaded Event   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Extensibility Namespace](topic1995.md) > [IApplicationPluginManager Interface](topic2021.md) : ApplicationPluginLoaded Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Occurs when an application plugin has been loaded into the application. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event ApplicationPluginLoaded As [ApplicationPluginLoadedEventHandler](topic2154.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IApplicationPluginManager](topic2021.md)
    Dim handler As [ApplicationPluginLoadedEventHandler](topic2154.md)
     
    AddHandler instance.ApplicationPluginLoaded, handler  
  
C#|   
---|---  
      
    
    event [ApplicationPluginLoadedEventHandler](topic2154.md) ApplicationPluginLoaded  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IApplicationPluginManager Interface](topic2021.md)   
[IApplicationPluginManager Members](topic2022.md)


