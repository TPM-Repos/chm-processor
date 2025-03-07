Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
EnsureValidRuleSnippet Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectUtility Class](topic4899.md) : EnsureValidRuleSnippet Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_formula_
    The formula to sample from.

_startIndex_
    The start index of the subsection.

_endIndex_
    The end index of the subsection.

Glossary Item Box

Ensures the given indices marks a valid subsection in the given formula. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function EnsureValidRuleSnippet( _
       ByVal _formula_ As String, _
       ByRef _startIndex_ As Integer, _
       ByRef _endIndex_ As Integer _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectUtility](topic4899.md)
    Dim formula As String
    Dim startIndex As Integer
    Dim endIndex As Integer
    Dim value As Boolean
     
    value = instance.EnsureValidRuleSnippet(formula, startIndex, endIndex)  
  
C#|   
---|---  
      
    
    public bool EnsureValidRuleSnippet( 
       string _formula_ ,
       ref int _startIndex_ ,
       ref int _endIndex_
    )  
  
#### Parameters

 _formula_
    The formula to sample from.
_startIndex_
    The start index of the subsection.
_endIndex_
    The end index of the subsection.

#### Return Value

Whether or not the given indices have been changed.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectUtility Class](topic4899.md)   
[ProjectUtility Members](topic4900.md)


