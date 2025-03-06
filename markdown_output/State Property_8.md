       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
State Property   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic305.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IHasState Interface](topic300.md) : State Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the individual states which make up current state of the object. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    ReadOnly Property State As Guid()  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IHasState](topic300.md)
    Dim value() As Guid
     
    value = instance.State  
  
C#|   
---|---  
      
    
    Guid[] State {get;}  
  
#### Property Value

An array of globally unique identifiers each of which represents a state, well-known application states are defined in [StandardStates](topic1067.md).

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IHasState Interface](topic300.md)   
[IHasState Members](topic301.md)

©2024 DriveWorks Ltd. All Rights Reserved.
