Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
LoadException Property   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Extensibility Namespace](topic1995.md) > [IApplicationPluginInfo Interface](topic2010.md) : LoadException Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

If an exception occurred loading the plugin, gets the exception that occurred. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    ReadOnly Property LoadException As Exception  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IApplicationPluginInfo](topic2010.md)
    Dim value As Exception
     
    value = instance.LoadException  
  
C#|   
---|---  
      
    
    Exception LoadException {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IApplicationPluginInfo Interface](topic2010.md)   
[IApplicationPluginInfo Members](topic2011.md)


