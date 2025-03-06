       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SolidWorksBatchHint Enumeration   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic1807.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) : SolidWorksBatchHint Enumeration  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Provides hints to the health monitor about a batch. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <FlagsAttribute()>
    Public Enum SolidWorksBatchHint 
       Inherits System.Enum  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SolidWorksBatchHint](topic1807.md)  
  
C#|   
---|---  
      
    
    [FlagsAttribute()]
    public enum SolidWorksBatchHint : System.Enum   
  
# Members

Member| Description  
---|---  
**None**|  No specific hints are assigned to the batch.  
**Single**|  The batch consists of a single model, therefore, if the "Restart After Batch" behavior is in play, the health monitor should consider coalescing batches before restarting SolidWorks for optimum efficiency.  
  
# Inheritance Hierarchy

System.Object  
System.ValueType  
System.Enum  
**DriveWorks.Applications.Autopilot.Extensibility.SolidWorksBatchHint**  


# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md)

©2024 DriveWorks Ltd. All Rights Reserved.
