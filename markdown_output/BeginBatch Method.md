![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
BeginBatch Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic1746.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) > [ISolidWorksHealthMonitor Interface](topic1741.md) : BeginBatch Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_hint_
    Provides hints to the monitor about the nature of the batch.

Glossary Item Box

Notifies the monitor of the intention to begin a batch of model generation. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function BeginBatch( _
       ByVal _hint_ As [SolidWorksBatchHint](topic1807.md) _
    ) As [ISolidWorksOperationBatch](topic1755.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ISolidWorksHealthMonitor](topic1741.md)
    Dim hint As [SolidWorksBatchHint](topic1807.md)
    Dim value As [ISolidWorksOperationBatch](topic1755.md)
     
    value = instance.BeginBatch(hint)  
  
C#|   
---|---  
      
    
    [ISolidWorksOperationBatch](topic1755.md) BeginBatch( 
       [SolidWorksBatchHint](topic1807.md) _hint_
    )  
  
#### Parameters

 _hint_
    Provides hints to the monitor about the nature of the batch.

#### Return Value

An operation batch which can be used to coordinate model generation.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ISolidWorksHealthMonitor Interface](topic1741.md)   
[ISolidWorksHealthMonitor Members](topic1742.md)

©2024 DriveWorks Ltd. All Rights Reserved.
