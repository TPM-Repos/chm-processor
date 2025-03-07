Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetApplicationPlugins Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Extensibility Namespace](topic1995.md) > [IApplicationPluginManager Interface](topic2021.md) : GetApplicationPlugins Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets an array of application plugins that are loaded into the application. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function GetApplicationPlugins() As [IApplicationPluginInfo()](topic2010.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IApplicationPluginManager](topic2021.md)
    Dim value() As [IApplicationPluginInfo](topic2010.md)
     
    value = instance.GetApplicationPlugins()  
  
C#|   
---|---  
      
    
    [IApplicationPluginInfo[]](topic2010.md) GetApplicationPlugins()  
  
#### Return Value

An array of information about the loaded application plugins.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IApplicationPluginManager Interface](topic2021.md)   
[IApplicationPluginManager Members](topic2022.md)


