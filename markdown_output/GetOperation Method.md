Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetOperation Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [Operations Class](topic11095.md) : GetOperation Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the operation to get.

Glossary Item Box

Gets the operation with the specified name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetOperation( _
       ByVal _name_ As String _
    ) As [Operation](topic11068.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [Operations](topic11095.md)
    Dim name As String
    Dim value As [Operation](topic11068.md)
     
    value = instance.GetOperation(name)  
  
C#|   
---|---  
      
    
    public [Operation](topic11068.md) GetOperation( 
       string _name_
    )  
  
#### Parameters

 _name_
    The name of the operation to get.

#### Return Value

The operation with the specified name.

# Exceptions

Exception| Description  
---|---  
[DriveWorks.ItemNotFoundException](topic3571.md)| The operation could not be found.  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[Operations Class](topic11095.md)   
[Operations Members](topic11096.md)


