       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Translate(String,Stream,Encoding) Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) > [ISpecificationAutomation Interface](topic1761.md) > [Translate Method](topic1768.md) : Translate(String,Stream,Encoding) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_fileName_
    The full path to the file name.

_data_
    A seekable stream containing the file data.

_encoding_
    The encoding to use when reading the file.

Glossary Item Box

Translates the data in the specified file. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Overloads Function Translate( _
       ByVal _fileName_ As String, _
       ByVal _data_ As Stream, _
       ByVal _encoding_ As Encoding _
    ) As [ISpecificationRequest()](topic1778.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ISpecificationAutomation](topic1761.md)
    Dim fileName As String
    Dim data As Stream
    Dim encoding As Encoding
    Dim value() As [ISpecificationRequest](topic1778.md)
     
    value = instance.Translate(fileName, data, encoding)  
  
C#|   
---|---  
      
    
    [ISpecificationRequest[]](topic1778.md) Translate( 
       string _fileName_ ,
       Stream _data_ ,
       Encoding _encoding_
    )  
  
#### Parameters

 _fileName_
    The full path to the file name.
_data_
    A seekable stream containing the file data.
_encoding_
    The encoding to use when reading the file.

#### Return Value

A null reference if no translator understands the file contents, otherwise, an array of specification requests.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ISpecificationAutomation Interface](topic1761.md)   
[ISpecificationAutomation Members](topic1762.md)   
[Overload List](topic1768.md)


