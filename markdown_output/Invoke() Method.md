![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Invoke() Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic8059.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [DialogButton Class](topic8051.md) > [Invoke Method](topic8058.md) : Invoke() Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Shows the dialog named by the [DialogName](topic8061.md) property. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function Invoke() As Boolean  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [DialogButton](topic8051.md)
    Dim value As Boolean
     
    value = instance.Invoke()  
  
C#|   
---|---  
      
    
    public bool Invoke()  
  
#### Return Value

True if the dialog was activated. The only time false will be returned is if the dialog is found, but a preexecution macro closes the specification, forcing the dialog not to be activated.

# ![](dotnetimages/collapse.gif)Exceptions

Exception| Description  
---|---  
System.InvalidOperationException| No specification is active.  
[DriveWorks.ItemNotFoundException](topic3571.md)| The dialog doesn't exist.  
  
# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[DialogButton Class](topic8051.md)   
[DialogButton Members](topic8052.md)   
[Overload List](topic8058.md)

©2024 DriveWorks Ltd. All Rights Reserved.
