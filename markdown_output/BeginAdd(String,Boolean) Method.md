Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
BeginAdd(String,Boolean) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [ItemList Class](topic8183.md) > [BeginAdd Method](topic8190.md) : BeginAdd(String,Boolean) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_formname_
    The name of the form to use in the adding process.

_showUserInterface_
    Whether or not to show the user interface.

Glossary Item Box

Starts the adding process for this item list. Informs the specification context that a dialog is being opened etc. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <EditorBrowsableAttribute(EditorBrowsableState.Advanced)>
    Public Overloads Sub BeginAdd( _
       ByVal _formname_ As String, _
       ByVal _showUserInterface_ As Boolean _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ItemList](topic8183.md)
    Dim formname As String
    Dim showUserInterface As Boolean
     
    instance.BeginAdd(formname, showUserInterface)  
  
C#|   
---|---  
      
    
    [EditorBrowsableAttribute(EditorBrowsableState.Advanced)]
    public void BeginAdd( 
       string _formname_ ,
       bool _showUserInterface_
    )  
  
#### Parameters

 _formname_
    The name of the form to use in the adding process.
_showUserInterface_
    Whether or not to show the user interface.

# Exceptions

Exception| Description  
---|---  
System.InvalidOperationException|  Thrown when not in a Specification.   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ItemList Class](topic8183.md)   
[ItemList Members](topic8184.md)   
[Overload List](topic8190.md)


