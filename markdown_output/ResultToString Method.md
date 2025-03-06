       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ResultToString Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [RuleResults Class](topic11136.md) : ResultToString Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_result_
    The result to convert.

_ci_
    The culture information to use for culture aware conversions.

Glossary Item Box

Takes the result of a rule calculation and coverts it to a string. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Function ResultToString( _
       ByVal _result_ As Object, _
       ByVal _ci_ As CultureInfo _
    ) As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim result As Object
    Dim ci As CultureInfo
    Dim value As String
     
    value = [RuleResults](topic11136.md).ResultToString(result, ci)  
  
C#|   
---|---  
      
    
    public static string ResultToString( 
       object _result_ ,
       CultureInfo _ci_
    )  
  
#### Parameters

 _result_
    The result to convert.
_ci_
    The culture information to use for culture aware conversions.

#### Return Value

A string representing the result.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[RuleResults Class](topic11136.md)   
[RuleResults Members](topic11137.md)


