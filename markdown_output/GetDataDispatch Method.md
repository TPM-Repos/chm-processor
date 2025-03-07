Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetDataDispatch Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ConnectionManager Class](topic2554.md) : GetDataDispatch Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_isArray_
    True if the result is going to be used in an array rule, and therefore should be delimited by | characters, false if a single value is expected.

_getDataString_
    The GetData string to execute.

Glossary Item Box

Performs a DriveWorks GetData operation given a GetData string. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetDataDispatch( _
       ByVal _isArray_ As Boolean, _
       ByVal _getDataString_ As String _
    ) As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ConnectionManager](topic2554.md)
    Dim isArray As Boolean
    Dim getDataString As String
    Dim value As String
     
    value = instance.GetDataDispatch(isArray, getDataString)  
  
C#|   
---|---  
      
    
    public string GetDataDispatch( 
       bool _isArray_ ,
       string _getDataString_
    )  
  
#### Parameters

 _isArray_
    True if the result is going to be used in an array rule, and therefore should be delimited by | characters, false if a single value is expected.
_getDataString_
    The GetData string to execute.

#### Return Value

The result of the GetData string.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ConnectionManager Class](topic2554.md)   
[ConnectionManager Members](topic2555.md)


