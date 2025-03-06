       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Translate(Stream,Encoding,String) Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) > [ISpecificationAutomation Interface](topic1761.md) > [Translate Method](topic1768.md) : Translate(Stream,Encoding,String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_data_
    A seekable stream containing the data to translate.

_encoding_
    The encoding to use when reading the data.

_mimeType_
    The MIME type of the stream contents.

Glossary Item Box

Translates the data in the specified stream. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Overloads Function Translate( _
       ByVal _data_ As Stream, _
       ByVal _encoding_ As Encoding, _
       ByVal _mimeType_ As String _
    ) As [ISpecificationRequest()](topic1778.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ISpecificationAutomation](topic1761.md)
    Dim data As Stream
    Dim encoding As Encoding
    Dim mimeType As String
    Dim value() As [ISpecificationRequest](topic1778.md)
     
    value = instance.Translate(data, encoding, mimeType)  
  
C#|   
---|---  
      
    
    [ISpecificationRequest[]](topic1778.md) Translate( 
       Stream _data_ ,
       Encoding _encoding_ ,
       string _mimeType_
    )  
  
#### Parameters

 _data_
    A seekable stream containing the data to translate.
_encoding_
    The encoding to use when reading the data.
_mimeType_
    The MIME type of the stream contents.

#### Return Value

A null reference if no translator understands the file contents, otherwise, an array of specification requests.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ISpecificationAutomation Interface](topic1761.md)   
[ISpecificationAutomation Members](topic1762.md)   
[Overload List](topic1768.md)


