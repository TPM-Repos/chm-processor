Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Instance Property   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Extensibility Namespace](topic1995.md) > [IApplicationPluginInfo Interface](topic2010.md) : Instance Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the instance of the plugin. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    ReadOnly Property Instance As [IApplicationPlugin](topic2004.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IApplicationPluginInfo](topic2010.md)
    Dim value As [IApplicationPlugin](topic2004.md)
     
    value = instance.Instance  
  
C#|   
---|---  
      
    
    [IApplicationPlugin](topic2004.md) Instance {get;}  
  
# Remarks

If an exception occurred loading the plugin, this will return a null reference.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IApplicationPluginInfo Interface](topic2010.md)   
[IApplicationPluginInfo Members](topic2011.md)


