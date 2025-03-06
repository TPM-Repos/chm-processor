![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Specify Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic1767.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) > [ISpecificationAutomation Interface](topic1761.md) : Specify Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_request_
    An instance of [ISpecificationRequest](topic1778.md) representing the data to be specified.

_waitForCompletion_
    True to wait for the specification to complete, false to queue the specification and return immediately.

Glossary Item Box

Starts a new specification based on the passed-in instance of [ISpecificationRequest](topic1778.md)

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub Specify( _
       ByVal _request_ As [ISpecificationRequest](topic1778.md), _
       ByVal _waitForCompletion_ As Boolean _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ISpecificationAutomation](topic1761.md)
    Dim request As [ISpecificationRequest](topic1778.md)
    Dim waitForCompletion As Boolean
     
    instance.Specify(request, waitForCompletion)  
  
C#|   
---|---  
      
    
    void Specify( 
       [ISpecificationRequest](topic1778.md) _request_ ,
       bool _waitForCompletion_
    )  
  
#### Parameters

 _request_
    An instance of [ISpecificationRequest](topic1778.md) representing the data to be specified.
_waitForCompletion_
    True to wait for the specification to complete, false to queue the specification and return immediately.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ISpecificationAutomation Interface](topic1761.md)   
[ISpecificationAutomation Members](topic1762.md)

©2024 DriveWorks Ltd. All Rights Reserved.
