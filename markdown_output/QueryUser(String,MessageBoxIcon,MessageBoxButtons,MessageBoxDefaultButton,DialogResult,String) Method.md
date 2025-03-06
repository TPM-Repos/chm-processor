![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
QueryUser(String,MessageBoxIcon,MessageBoxButtons,MessageBoxDefaultButton,DialogResult,String) Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IInteraction Interface](topic321.md) > [QueryUser Method](topic326.md) : QueryUser(String,MessageBoxIcon,MessageBoxButtons,MessageBoxDefaultButton,DialogResult,String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_question_
    The question to ask the user.

_icon_
    The icon shown in the message box.

_buttons_
    The buttons to show in the message box.

_defaultButton_
    The button to set as the default in the message box.

_defaultResponse_
    The default response to return if the application is running non-interactively.

_helpTopic_
    A help topic to be shown if the user requests help.

Glossary Item Box

Asks the user to provide a response to a prompt. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Overloads Function QueryUser( _
       ByVal _question_ As String, _
       ByVal _icon_ As MessageBoxIcon, _
       ByVal _buttons_ As MessageBoxButtons, _
       ByVal _defaultButton_ As MessageBoxDefaultButton, _
       ByVal _defaultResponse_ As DialogResult, _
       ByVal _helpTopic_ As String _
    ) As DialogResult  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [IInteraction](topic321.md)
    Dim question As String
    Dim icon As MessageBoxIcon
    Dim buttons As MessageBoxButtons
    Dim defaultButton As MessageBoxDefaultButton
    Dim defaultResponse As DialogResult
    Dim helpTopic As String
    Dim value As DialogResult
     
    value = instance.QueryUser(question, icon, buttons, defaultButton, defaultResponse, helpTopic)  
  
C#|   
---|---  
      
    
    DialogResult QueryUser( 
       string _question_ ,
       MessageBoxIcon _icon_ ,
       MessageBoxButtons _buttons_ ,
       MessageBoxDefaultButton _defaultButton_ ,
       DialogResult _defaultResponse_ ,
       string _helpTopic_
    )  
  
#### Parameters

 _question_
    The question to ask the user.
_icon_
    The icon shown in the message box.
_buttons_
    The buttons to show in the message box.
_defaultButton_
    The button to set as the default in the message box.
_defaultResponse_
    The default response to return if the application is running non-interactively.
_helpTopic_
    A help topic to be shown if the user requests help.

#### Return Value

The response chosen by the user.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IInteraction Interface](topic321.md)   
[IInteraction Members](topic322.md)   
[Overload List](topic326.md)


