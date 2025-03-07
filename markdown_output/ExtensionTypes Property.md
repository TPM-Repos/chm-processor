Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ExtensionTypes Property   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Extensibility Namespace](topic1995.md) > [ILibraryInfo Interface](topic2055.md) : ExtensionTypes Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the extension types in the assembly. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    ReadOnly Property ExtensionTypes As Type()  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ILibraryInfo](topic2055.md)
    Dim value() As Type
     
    value = instance.ExtensionTypes  
  
C#|   
---|---  
      
    
    Type[] ExtensionTypes {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ILibraryInfo Interface](topic2055.md)   
[ILibraryInfo Members](topic2056.md)


