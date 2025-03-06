![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RegisterJobQueue Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic2977.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [Group Class](topic2958.md) : RegisterJobQueue Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_jobType_
    The type of job that the queue will process.

Glossary Item Box

Registers a queue of jobs within DriveWorks that need to be processed. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function RegisterJobQueue( _
       ByVal _jobType_ As String _
    ) As [JobQueue](topic3594.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [Group](topic2958.md)
    Dim jobType As String
    Dim value As [JobQueue](topic3594.md)
     
    value = instance.RegisterJobQueue(jobType)  
  
C#|   
---|---  
      
    
    public [JobQueue](topic3594.md) RegisterJobQueue( 
       string _jobType_
    )  
  
#### Parameters

 _jobType_
    The type of job that the queue will process.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[Group Class](topic2958.md)   
[Group Members](topic2959.md)

©2024 DriveWorks Ltd. All Rights Reserved.
