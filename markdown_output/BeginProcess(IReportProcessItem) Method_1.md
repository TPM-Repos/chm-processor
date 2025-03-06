![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
BeginProcess(IReportProcessItem) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic10374.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Reporting Namespace](topic10334.md) > [CompositeReportWriter Class](topic10363.md) > [BeginProcess Method](topic10372.md) : BeginProcess(IReportProcessItem) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_processItem_
    The process item to use to start the process

Glossary Item Box

Begins a process. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Sub BeginProcess( _
       ByVal _processItem_ As [IReportProcessItem](topic2285.md) _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [CompositeReportWriter](topic10363.md)
    Dim processItem As [IReportProcessItem](topic2285.md)
     
    instance.BeginProcess(processItem)  
  
C#|   
---|---  
      
    
    public void BeginProcess( 
       [IReportProcessItem](topic2285.md) _processItem_
    )  
  
#### Parameters

 _processItem_
    The process item to use to start the process

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[CompositeReportWriter Class](topic10363.md)   
[CompositeReportWriter Members](topic10364.md)   
[Overload List](topic10372.md)

©2024 DriveWorks Ltd. All Rights Reserved.
