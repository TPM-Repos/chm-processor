Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetMessage Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectMessages Class](topic4627.md) : GetMessage Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_code_
    The code of the message to retrieve.

Glossary Item Box

Gets the message with the specified display name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public MustOverride Function GetMessage( _
       ByVal _code_ As Integer _
    ) As [ProjectMessage](topic4601.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectMessages](topic4627.md)
    Dim code As Integer
    Dim value As [ProjectMessage](topic4601.md)
     
    value = instance.GetMessage(code)  
  
C#|   
---|---  
      
    
    public abstract [ProjectMessage](topic4601.md) GetMessage( 
       int _code_
    )  
  
#### Parameters

 _code_
    The code of the message to retrieve.

# Exceptions

Exception| Description  
---|---  
[ItemNotFoundException](topic3571.md)| Thrown when no messages with the specified display name exists.  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectMessages Class](topic4627.md)   
[ProjectMessages Members](topic4628.md)


