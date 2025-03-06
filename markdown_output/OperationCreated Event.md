![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
OperationCreated Event   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic11109.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [Operations Class](topic11095.md) : OperationCreated Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Occurs when an operation is created. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event OperationCreated As [OperationEventHandler](topic11820.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [Operations](topic11095.md)
    Dim handler As [OperationEventHandler](topic11820.md)
     
    AddHandler instance.OperationCreated, handler  
  
C#|   
---|---  
      
    
    public event [OperationEventHandler](topic11820.md) OperationCreated  
  
# ![](dotnetimages/collapse.gif)Event Data

The event handler receives an argument of type [OperationEventArgs](topic11084.md) containing data related to this event. The following **OperationEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[Operation](topic11094.md)| Gets the operation which is the target of the event.   
  
# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[Operations Class](topic11095.md)   
[Operations Members](topic11096.md)

©2024 DriveWorks Ltd. All Rights Reserved.
