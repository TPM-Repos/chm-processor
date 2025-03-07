Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
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

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub AddChange( _
       ByVal _title_ As String, _
       ByVal _applicator_ As Action _
    )   
  
Visual Basic (Usage)| Copy Code  
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

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[PendingChangeEventArgs Class](topic890.md)   
[PendingChangeEventArgs Members](topic891.md)


