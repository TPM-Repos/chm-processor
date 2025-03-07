Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
BeginEdit(String) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [ItemList Class](topic8183.md) > [BeginEdit Method](topic8196.md) : BeginEdit(String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_formName_
    The name of the form to use in the editing process.

Glossary Item Box

Starts the editing process for this item list. Informs the specification context that a dialog is being opened etc. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <EditorBrowsableAttribute(EditorBrowsableState.Advanced)>
    Public Overloads Sub BeginEdit( _
       ByVal _formName_ As String _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ItemList](topic8183.md)
    Dim formName As String
     
    instance.BeginEdit(formName)  
  
C#|   
---|---  
      
    
    [EditorBrowsableAttribute(EditorBrowsableState.Advanced)]
    public void BeginEdit( 
       string _formName_
    )  
  
#### Parameters

 _formName_
    The name of the form to use in the editing process.

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
[Overload List](topic8196.md)


