       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SpecificationDialogMessage Constructor   
  
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

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _specification_ As [SpecificationContext](topic11149.md), _
       ByVal _messageBody_ As String, _
       Optional ByVal _messageTitle_ As String, _
       Optional ByVal _messageIcon_ As MessageBoxIcon, _
       Optional ByVal _messageButtons_ As MessageBoxButtons _
    )  
  
Visual Basic (Usage)| Copy Code  
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

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SpecificationDialogMessage Class](topic5334.md)   
[SpecificationDialogMessage Members](topic5335.md)


