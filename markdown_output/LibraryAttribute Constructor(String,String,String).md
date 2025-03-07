Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
LibraryAttribute Constructor(String,String,String)   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Extensibility Namespace](topic7150.md) > [LibraryAttribute Class](topic7201.md) > [LibraryAttribute Constructor](topic7207.md) : LibraryAttribute Constructor(String,String,String)  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_invariantName_
    The invariant name of the extension library.

_displayName_
    Specifies the display name of the extension library.

_description_
    Specifies a brief description of the extension library.

Glossary Item Box

Initializes a new instance of the [LibraryAttribute](topic7201.md) type. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _invariantName_ As String, _
       ByVal _displayName_ As String, _
       ByVal _description_ As String _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim invariantName As String
    Dim displayName As String
    Dim description As String
     
    Dim instance As New [LibraryAttribute](topic7201.md)(invariantName, displayName, description)  
  
C#|   
---|---  
      
    
    public LibraryAttribute( 
       string _invariantName_ ,
       string _displayName_ ,
       string _description_
    )  
  
#### Parameters

 _invariantName_
    The invariant name of the extension library.
_displayName_
    Specifies the display name of the extension library.
_description_
    Specifies a brief description of the extension library.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[LibraryAttribute Class](topic7201.md)   
[LibraryAttribute Members](topic7202.md)   
[Overload List](topic7207.md)


