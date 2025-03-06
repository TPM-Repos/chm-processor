       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RootComponentIds Property   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic6112.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components Namespace](topic6089.md) > [IReleasedComponentReferenceTree Interface](topic6106.md) : RootComponentIds Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the unique identifiers of all of the root components in the reference tree. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    ReadOnly Property RootComponentIds As Guid()  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IReleasedComponentReferenceTree](topic6106.md)
    Dim value() As Guid
     
    value = instance.RootComponentIds  
  
C#|   
---|---  
      
    
    Guid[] RootComponentIds {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IReleasedComponentReferenceTree Interface](topic6106.md)   
[IReleasedComponentReferenceTree Members](topic6107.md)

©2024 DriveWorks Ltd. All Rights Reserved.
