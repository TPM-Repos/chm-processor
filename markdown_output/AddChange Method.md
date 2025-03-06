![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AddChange Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [PendingChangeEventArgs Class](topic890.md) : AddChange Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_title_
    A short title of what the pending change is for.

_applicator_
    A method that when called with apply the pending change.

Glossary Item Box

Registers a change with the event raiser, to be applied if deemed necessary. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub AddChange( _
       ByVal _title_ As String, _
       ByVal _applicator_ As Action _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [PendingChangeEventArgs](topic890.md)
    Dim title As String
    Dim applicator As Action
     
    instance.AddChange(title, applicator)  
  
C#|   
---|---  
      
    
    public void AddChange( 
       string _title_ ,
       Action _applicator_
    )  
  
#### Parameters

 _title_
    A short title of what the pending change is for.
_applicator_
    A method that when called with apply the pending change.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[PendingChangeEventArgs Class](topic890.md)   
[PendingChangeEventArgs Members](topic891.md)


