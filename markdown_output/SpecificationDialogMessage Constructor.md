![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SpecificationDialogMessage Constructor   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic5340.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [SpecificationDialogMessage Class](topic5334.md) : SpecificationDialogMessage Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_specification_
    The specification that this message is is being raised from.

_messageBody_
    The main text that will appear in the message to the user.

_messageTitle_
    The title for the message.

_messageIcon_
    The type of icon that will appear next the message.

_messageButtons_
    The available options that the user will have to respond with.

Glossary Item Box

Creates a new instance of the [SpecificationDialogMessage](topic5334.md) class. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _specification_ As [SpecificationContext](topic11149.md), _
       ByVal _messageBody_ As String, _
       Optional ByVal _messageTitle_ As String, _
       Optional ByVal _messageIcon_ As MessageBoxIcon, _
       Optional ByVal _messageButtons_ As MessageBoxButtons _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim specification As [SpecificationContext](topic11149.md)
    Dim messageBody As String
    Dim messageTitle As String
    Dim messageIcon As MessageBoxIcon
    Dim messageButtons As MessageBoxButtons
     
    Dim instance As New [SpecificationDialogMessage](topic5334.md)(specification, messageBody, messageTitle, messageIcon, messageButtons)  
  
C#|   
---|---  
      
    
    public SpecificationDialogMessage( 
       [SpecificationContext](topic11149.md) _specification_ ,
       string _messageBody_ ,
       string _messageTitle_ ,
       MessageBoxIcon _messageIcon_ ,
       MessageBoxButtons _messageButtons_
    )  
  
#### Parameters

 _specification_
    The specification that this message is is being raised from.
_messageBody_
    The main text that will appear in the message to the user.
_messageTitle_
    The title for the message.
_messageIcon_
    The type of icon that will appear next the message.
_messageButtons_
    The available options that the user will have to respond with.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[SpecificationDialogMessage Class](topic5334.md)   
[SpecificationDialogMessage Members](topic5335.md)

©2024 DriveWorks Ltd. All Rights Reserved.
