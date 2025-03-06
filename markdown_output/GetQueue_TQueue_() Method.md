![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

_TQueue_
    The type of service to search for.

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetQueue<TQueue>() Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic1651.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) > [IAutopilotQueueManager Interface](topic1643.md) > [GetQueue Method](topic1649.md) : GetQueue<TQueue>() Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets any queues which implement the specified service. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Overloads Function GetQueue(Of TQueue)() As IEnumerable(Of TQueue)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [IAutopilotQueueManager](topic1643.md)
    Dim value As IEnumerable(Of TQueue)
     
    value = instance.GetQueue(Of TQueue)()  
  
C#|   
---|---  
      
    
    IEnumerable<TQueue> GetQueue<TQueue>()  
  
#### Type Parameters

_TQueue_
    The type of service to search for.

#### Return Value

A collection of queues matching the search criteria.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IAutopilotQueueManager Interface](topic1643.md)   
[IAutopilotQueueManager Members](topic1644.md)   
[Overload List](topic1649.md)

©2024 DriveWorks Ltd. All Rights Reserved.
