       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TestMode Property   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic6390.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components Namespace](topic6089.md) > [ReleaseEnvironment Class](topic6379.md) : TestMode Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets/sets whether the release is happening in Test Mode. This means that during the release of components, duplicate ones should be fully processed. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Property TestMode As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ReleaseEnvironment](topic6379.md)
    Dim value As Boolean
     
    instance.TestMode = value
     
    value = instance.TestMode  
  
C#|   
---|---  
      
    
    public bool TestMode {get; set;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReleaseEnvironment Class](topic6379.md)   
[ReleaseEnvironment Members](topic6380.md)

©2024 DriveWorks Ltd. All Rights Reserved.
