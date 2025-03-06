       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TransitionName Property   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic1786.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) > [ISpecificationRequest Interface](topic1778.md) : TransitionName Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the name of the transition to invoke when the specification has been filled in. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Property TransitionName As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ISpecificationRequest](topic1778.md)
    Dim value As String
     
    instance.TransitionName = value
     
    value = instance.TransitionName  
  
C#|   
---|---  
      
    
    string TransitionName {get; set;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ISpecificationRequest Interface](topic1778.md)   
[ISpecificationRequest Members](topic1779.md)

©2024 DriveWorks Ltd. All Rights Reserved.
