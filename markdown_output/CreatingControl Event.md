![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreatingControl Event   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic8111.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [Form Class](topic8086.md) : CreatingControl Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when a control is being created. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event CreatingControl As EventHandler(Of CreatingControlEventArgs)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [Form](topic8086.md)
    Dim handler As EventHandler(Of CreatingControlEventArgs)
     
    AddHandler instance.CreatingControl, handler  
  
C#|   
---|---  
      
    
    public event EventHandler<CreatingControlEventArgs> CreatingControl  
  
# ![](dotnetimages/collapse.gif)Event Data

The event handler receives an argument of type [CreatingControlEventArgs](topic7826.md) containing data related to this event. The following **CreatingControlEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[Cancel](topic7835.md)| Whether or not the creation of the control will be cancelled.   
[ControlName](topic7836.md)| The name of the control that is being created.   
[ControlType](topic7837.md)| The type of control that is being created.   
  
# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[Form Class](topic8086.md)   
[Form Members](topic8087.md)

©2024 DriveWorks Ltd. All Rights Reserved.
