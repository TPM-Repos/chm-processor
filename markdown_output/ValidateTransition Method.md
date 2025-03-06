       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ValidateTransition Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic13319.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Utility Namespace](topic13190.md) > [ValidationUtility Class](topic13287.md) : ValidateTransition Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_transition_
    The name to validate.

Glossary Item Box

Validates a DriveWorks transition name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Function ValidateTransition( _
       ByVal _transition_ As String _
    ) As [ValidateNameResult](topic13193.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim transition As String
    Dim value As [ValidateNameResult](topic13193.md)
     
    value = [ValidationUtility](topic13287.md).ValidateTransition(transition)  
  
C#|   
---|---  
      
    
    public static [ValidateNameResult](topic13193.md) ValidateTransition( 
       string _transition_
    )  
  
#### Parameters

 _transition_
    The name to validate.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ValidationUtility Class](topic13287.md)   
[ValidationUtility Members](topic13288.md)

©2024 DriveWorks Ltd. All Rights Reserved.
