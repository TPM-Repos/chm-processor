       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RuleResultToDisplayString Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic4922.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectUtility Class](topic4899.md) : RuleResultToDisplayString Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_value_
    The value to convert.

_ci_
    The culture info to use, if null is specified, the current UI culture is used.

Glossary Item Box

Converts the specified rule result to a string suitable for display. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function RuleResultToDisplayString( _
       ByVal _value_ As Object, _
       ByVal _ci_ As CultureInfo _
    ) As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectUtility](topic4899.md)
    Dim value As Object
    Dim ci As CultureInfo
    Dim value As String
     
    value = instance.RuleResultToDisplayString(value, ci)  
  
C#|   
---|---  
      
    
    public string RuleResultToDisplayString( 
       object _value_ ,
       CultureInfo _ci_
    )  
  
#### Parameters

 _value_
    The value to convert.
_ci_
    The culture info to use, if null is specified, the current UI culture is used.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectUtility Class](topic4899.md)   
[ProjectUtility Members](topic4900.md)

©2024 DriveWorks Ltd. All Rights Reserved.
