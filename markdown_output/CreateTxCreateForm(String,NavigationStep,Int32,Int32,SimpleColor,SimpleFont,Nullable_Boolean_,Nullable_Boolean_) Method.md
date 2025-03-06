![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxCreateForm(String,NavigationStep,Int32,Int32,SimpleColor,SimpleFont,Nullable<Boolean>,Nullable<Boolean>) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) > [CreateTxCreateForm Method](topic13050.md) : CreateTxCreateForm(String,NavigationStep,Int32,Int32,SimpleColor,SimpleFont,Nullable<Boolean>,Nullable<Boolean>) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the new form.

_nextStep_
    The next step, from this form.

_left_
    The horrizontal position of the form.

_top_
    The vertical position of the form.

_backgroundColor_
    The background color to apply to the form.

_defaultFont_
    The default font to apply to the form.

_showStandardNavigation_
    Specifies whether the form should show standard navigation.

_showTaskList_
    Specifies whether the form should show the task list.

Glossary Item Box

Creates a transaction which, when committed, will create a form with the given properties, only name is needed. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function CreateTxCreateForm( _
       ByVal _name_ As String, _
       ByVal _nextStep_ As [NavigationStep](topic10175.md), _
       ByVal _left_ As Integer, _
       ByVal _top_ As Integer, _
       ByVal _backgroundColor_ As [SimpleColor](topic8856.md), _
       ByVal _defaultFont_ As [SimpleFont](topic8882.md), _
       ByVal _showStandardNavigation_ As Nullable(Of Boolean), _
       ByVal _showTaskList_ As Nullable(Of Boolean) _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim name As String
    Dim nextStep As [NavigationStep](topic10175.md)
    Dim left As Integer
    Dim top As Integer
    Dim backgroundColor As [SimpleColor](topic8856.md)
    Dim defaultFont As [SimpleFont](topic8882.md)
    Dim showStandardNavigation As Nullable(Of Boolean)
    Dim showTaskList As Nullable(Of Boolean)
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxCreateForm(name, nextStep, left, top, backgroundColor, defaultFont, showStandardNavigation, showTaskList)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxCreateForm( 
       string _name_ ,
       [NavigationStep](topic10175.md) _nextStep_ ,
       int _left_ ,
       int _top_ ,
       [SimpleColor](topic8856.md) _backgroundColor_ ,
       [SimpleFont](topic8882.md) _defaultFont_ ,
       Nullable<bool> _showStandardNavigation_ ,
       Nullable<bool> _showTaskList_
    )  
  
#### Parameters

 _name_
    The name of the new form.
_nextStep_
    The next step, from this form.
_left_
    The horrizontal position of the form.
_top_
    The vertical position of the form.
_backgroundColor_
    The background color to apply to the form.
_defaultFont_
    The default font to apply to the form.
_showStandardNavigation_
    Specifies whether the form should show standard navigation.
_showTaskList_
    Specifies whether the form should show the task list.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)   
[Overload List](topic13050.md)


