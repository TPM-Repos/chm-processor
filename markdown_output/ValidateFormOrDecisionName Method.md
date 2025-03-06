       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ValidateFormOrDecisionName Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic13308.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Utility Namespace](topic13190.md) > [ValidationUtility Class](topic13287.md) : ValidateFormOrDecisionName Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name to validate.

Glossary Item Box

Validates a DriveWorks form or decision name 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Function ValidateFormOrDecisionName( _
       ByVal _name_ As String _
    ) As [ValidateNameResult](topic13193.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim name As String
    Dim value As [ValidateNameResult](topic13193.md)
     
    value = [ValidationUtility](topic13287.md).ValidateFormOrDecisionName(name)  
  
C#|   
---|---  
      
    
    public static [ValidateNameResult](topic13193.md) ValidateFormOrDecisionName( 
       string _name_
    )  
  
#### Parameters

 _name_
    The name to validate.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ValidationUtility Class](topic13287.md)   
[ValidationUtility Members](topic13288.md)

©2024 DriveWorks Ltd. All Rights Reserved.
