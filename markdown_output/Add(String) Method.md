Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Add(String) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [SpecificationMacros Class](topic11467.md) > [Add Method](topic11473.md) : Add(String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the macro.

Glossary Item Box

Adds a new macro with the given name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function Add( _
       ByVal _name_ As String _
    ) As [SpecificationMacro](topic11429.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SpecificationMacros](topic11467.md)
    Dim name As String
    Dim value As [SpecificationMacro](topic11429.md)
     
    value = instance.Add(name)  
  
C#|   
---|---  
      
    
    public [SpecificationMacro](topic11429.md) Add( 
       string _name_
    )  
  
#### Parameters

 _name_
    The name of the macro.

#### Return Value

The newly added macro.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SpecificationMacros Class](topic11467.md)   
[SpecificationMacros Members](topic11468.md)   
[Overload List](topic11473.md)


