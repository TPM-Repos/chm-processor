Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Assembly Property   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Extensibility Namespace](topic1995.md) > [IApplicationPluginInfo Interface](topic2010.md) : Assembly Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the library from which the plugin was loaded. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    ReadOnly Property Assembly As [ILibraryInfo](topic2055.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IApplicationPluginInfo](topic2010.md)
    Dim value As [ILibraryInfo](topic2055.md)
     
    value = instance.Assembly  
  
C#|   
---|---  
      
    
    [ILibraryInfo](topic2055.md) Assembly {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IApplicationPluginInfo Interface](topic2010.md)   
[IApplicationPluginInfo Members](topic2011.md)


