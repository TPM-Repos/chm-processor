       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ResetSpecificationIdPool Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic3396.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupSpecifications Class](topic3355.md) : ResetSpecificationIdPool Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Clears the specification Id pool for this group. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub ResetSpecificationIdPool()   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupSpecifications](topic3355.md)
     
    instance.ResetSpecificationIdPool()  
  
C#|   
---|---  
      
    
    public void ResetSpecificationIdPool()  
  
# Exceptions

Exception| Description  
---|---  
System.UnauthorizedAccessException| Thrown when the current user is working in global specification id pool and does not have the edit all specifications permission.  
System.InvalidOperationException| Thrown when there are current specifications in the group.  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupSpecifications Class](topic3355.md)   
[GroupSpecifications Members](topic3356.md)

©2024 DriveWorks Ltd. All Rights Reserved.
