Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetObjectData Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupVersionInformation Class](topic3446.md) : GetObjectData Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_info_
    

_context_
    

Glossary Item Box

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub GetObjectData( _
       ByVal _info_ As SerializationInfo, _
       ByVal _context_ As StreamingContext _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupVersionInformation](topic3446.md)
    Dim info As SerializationInfo
    Dim context As StreamingContext
     
    instance.GetObjectData(info, context)  
  
C#|   
---|---  
      
    
    public void GetObjectData( 
       SerializationInfo _info_ ,
       StreamingContext _context_
    )  
  
#### Parameters

 _info_
    
_context_
    

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupVersionInformation Class](topic3446.md)   
[GroupVersionInformation Members](topic3447.md)


