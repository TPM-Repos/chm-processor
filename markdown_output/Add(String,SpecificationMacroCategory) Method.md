Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Add(String,SpecificationMacroCategory) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [SpecificationMacros Class](topic11467.md) > [Add Method](topic11473.md) : Add(String,SpecificationMacroCategory) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the macro.

_category_
    The category that the macro belongs to.

Glossary Item Box

Adds a new macro with the given name and category 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function Add( _
       ByVal _name_ As String, _
       ByVal _category_ As [SpecificationMacroCategory](topic5359.md) _
    ) As [SpecificationMacro](topic11429.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SpecificationMacros](topic11467.md)
    Dim name As String
    Dim category As [SpecificationMacroCategory](topic5359.md)
    Dim value As [SpecificationMacro](topic11429.md)
     
    value = instance.Add(name, category)  
  
C#|   
---|---  
      
    
    public [SpecificationMacro](topic11429.md) Add( 
       string _name_ ,
       [SpecificationMacroCategory](topic5359.md) _category_
    )  
  
#### Parameters

 _name_
    The name of the macro.
_category_
    The category that the macro belongs to.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SpecificationMacros Class](topic11467.md)   
[SpecificationMacros Members](topic11468.md)   
[Overload List](topic11473.md)


