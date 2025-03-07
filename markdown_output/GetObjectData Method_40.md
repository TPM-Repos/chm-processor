Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetObjectData Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [UnknownDocumentProviderException Class](topic5772.md) : GetObjectData Method  
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
      
    
    Public Overrides Sub GetObjectData( _
       ByVal _info_ As SerializationInfo, _
       ByVal _context_ As StreamingContext _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [UnknownDocumentProviderException](topic5772.md)
    Dim info As SerializationInfo
    Dim context As StreamingContext
     
    instance.GetObjectData(info, context)  
  
C#|   
---|---  
      
    
    public override void GetObjectData( 
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

[UnknownDocumentProviderException Class](topic5772.md)   
[UnknownDocumentProviderException Members](topic5773.md)


