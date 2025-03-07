Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AddInput Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Connectors.Database Namespace](topic6754.md) > [DatabaseConnectorConfiguration Class](topic6756.md) : AddInput Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_fieldName_
    The database field name to bind to.

_inputName_
    The DriveWorks input name to bind to.

Glossary Item Box

Adds a new input bindings for this configuration. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub AddInput( _
       ByVal _fieldName_ As String, _
       ByVal _inputName_ As String _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [DatabaseConnectorConfiguration](topic6756.md)
    Dim fieldName As String
    Dim inputName As String
     
    instance.AddInput(fieldName, inputName)  
  
C#|   
---|---  
      
    
    public void AddInput( 
       string _fieldName_ ,
       string _inputName_
    )  
  
#### Parameters

 _fieldName_
    The database field name to bind to.
_inputName_
    The DriveWorks input name to bind to.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[DatabaseConnectorConfiguration Class](topic6756.md)   
[DatabaseConnectorConfiguration Members](topic6757.md)


