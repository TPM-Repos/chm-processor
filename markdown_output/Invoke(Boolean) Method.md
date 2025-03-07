Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Invoke(Boolean) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [DialogButton Class](topic8051.md) > [Invoke Method](topic8058.md) : Invoke(Boolean) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_showUserInterface_
    Whether or not to show the user interface.

Glossary Item Box

Shows the dialog named by the [DialogName](topic8061.md) property. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function Invoke( _
       ByVal _showUserInterface_ As Boolean _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [DialogButton](topic8051.md)
    Dim showUserInterface As Boolean
    Dim value As Boolean
     
    value = instance.Invoke(showUserInterface)  
  
C#|   
---|---  
      
    
    public bool Invoke( 
       bool _showUserInterface_
    )  
  
#### Parameters

 _showUserInterface_
    Whether or not to show the user interface.

#### Return Value

True if the dialog was activated. The only time false will be returned is if the dialog is found, but a preexecution macro closes the specification, forcing the dialog not to be activated.

# Exceptions

Exception| Description  
---|---  
System.InvalidOperationException| No specification is active.  
[DriveWorks.ItemNotFoundException](topic3571.md)| The dialog doesn't exist.  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[DialogButton Class](topic8051.md)   
[DialogButton Members](topic8052.md)   
[Overload List](topic8058.md)


