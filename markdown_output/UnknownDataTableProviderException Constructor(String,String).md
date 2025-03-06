       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
UnknownDataTableProviderException Constructor(String,String)   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [UnknownDataTableProviderException Class](topic5759.md) > [UnknownDataTableProviderException Constructor](topic5765.md) : UnknownDataTableProviderException Constructor(String,String)  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_dataTableName_
    The name of the table.

_typeName_
    The full name of the unknown type.

Glossary Item Box

Creates a new instance of the [UnknownDataTableProviderException](topic5759.md) class. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _dataTableName_ As String, _
       ByVal _typeName_ As String _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim dataTableName As String
    Dim typeName As String
     
    Dim instance As New [UnknownDataTableProviderException](topic5759.md)(dataTableName, typeName)  
  
C#|   
---|---  
      
    
    public UnknownDataTableProviderException( 
       string _dataTableName_ ,
       string _typeName_
    )  
  
#### Parameters

 _dataTableName_
    The name of the table.
_typeName_
    The full name of the unknown type.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[UnknownDataTableProviderException Class](topic5759.md)   
[UnknownDataTableProviderException Members](topic5760.md)   
[Overload List](topic5765.md)


