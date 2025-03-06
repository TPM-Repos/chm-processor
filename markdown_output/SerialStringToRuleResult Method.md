       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SerialStringToRuleResult Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic4923.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectUtility Class](topic4899.md) : SerialStringToRuleResult Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_value_
    The value to convert.

Glossary Item Box

Converts the specified serialized string to a value. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Function SerialStringToRuleResult( _
       ByVal _value_ As String _
    ) As Object  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim value As String
    Dim value As Object
     
    value = [ProjectUtility](topic4899.md).SerialStringToRuleResult(value)  
  
C#|   
---|---  
      
    
    public static object SerialStringToRuleResult( 
       string _value_
    )  
  
#### Parameters

 _value_
    The value to convert.

#### Return Value

The converted value.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectUtility Class](topic4899.md)   
[ProjectUtility Members](topic4900.md)

©2024 DriveWorks Ltd. All Rights Reserved.
