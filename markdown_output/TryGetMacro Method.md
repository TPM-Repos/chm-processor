       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TryGetMacro Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic11480.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [SpecificationMacros Class](topic11467.md) : TryGetMacro Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_macroName_
    The name of the macro to get.

_macro_
    Receives the macro if found.

Glossary Item Box

Attempts to get the macro with the given name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function TryGetMacro( _
       ByVal _macroName_ As String, _
       ByRef _macro_ As [SpecificationMacro](topic11429.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SpecificationMacros](topic11467.md)
    Dim macroName As String
    Dim macro As [SpecificationMacro](topic11429.md)
    Dim value As Boolean
     
    value = instance.TryGetMacro(macroName, macro)  
  
C#|   
---|---  
      
    
    public bool TryGetMacro( 
       string _macroName_ ,
       ref [SpecificationMacro](topic11429.md) _macro_
    )  
  
#### Parameters

 _macroName_
    The name of the macro to get.
_macro_
    Receives the macro if found.

#### Return Value

True if a macro with the given name was found and returned, otherwise false.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SpecificationMacros Class](topic11467.md)   
[SpecificationMacros Members](topic11468.md)

©2024 DriveWorks Ltd. All Rights Reserved.
