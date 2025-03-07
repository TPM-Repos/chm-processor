Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetMacro Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [SpecificationMacros Class](topic11467.md) : GetMacro Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_macroName_
    The name of the macro to retrieve.

Glossary Item Box

Gets the macro with the specified name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetMacro( _
       ByVal _macroName_ As String _
    ) As [SpecificationMacro](topic11429.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SpecificationMacros](topic11467.md)
    Dim macroName As String
    Dim value As [SpecificationMacro](topic11429.md)
     
    value = instance.GetMacro(macroName)  
  
C#|   
---|---  
      
    
    public [SpecificationMacro](topic11429.md) GetMacro( 
       string _macroName_
    )  
  
#### Parameters

 _macroName_
    The name of the macro to retrieve.

# Exceptions

Exception| Description  
---|---  
[DriveWorks.ItemNotFoundException](topic3571.md)| Thrown when no macro with the specified name exists.  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SpecificationMacros Class](topic11467.md)   
[SpecificationMacros Members](topic11468.md)


