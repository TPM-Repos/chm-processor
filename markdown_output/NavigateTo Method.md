Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
NavigateTo Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [SpecificationContext Class](topic11149.md) : NavigateTo Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_formName_
    The name of the form to navigate to.

Glossary Item Box

Navigates to a specified form in a running specification. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function NavigateTo( _
       ByVal _formName_ As String _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SpecificationContext](topic11149.md)
    Dim formName As String
    Dim value As Boolean
     
    value = instance.NavigateTo(formName)  
  
C#|   
---|---  
      
    
    public bool NavigateTo( 
       string _formName_
    )  
  
#### Parameters

 _formName_
    The name of the form to navigate to.

#### Return Value

True if the navigation operation succeeds, otherwise false.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SpecificationContext Class](topic11149.md)   
[SpecificationContext Members](topic11150.md)


