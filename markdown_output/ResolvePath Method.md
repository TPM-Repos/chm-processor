ResolvePath Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectUtility Class](topic4899.md) : ResolvePath Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_filePath_
    The file path to resolve, e.g. "<Project>\SomeFile.txt"

_relativePathBehavior_
    The behavior of the resolution if the file path specified is relative rather than qualified with a standard prefix.

Glossary Item Box

Resolves a prefixed file path. See remarks for details. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function ResolvePath( _
       ByVal _filePath_ As String, _
       ByVal _relativePathBehavior_ As [RelativeToDirectory](topic2359.md) _
    ) As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectUtility](topic4899.md)
    Dim filePath As String
    Dim relativePathBehavior As [RelativeToDirectory](topic2359.md)
    Dim value As String
     
    value = instance.ResolvePath(filePath, relativePathBehavior)  
  
C#|   
---|---  
      
    
    public string ResolvePath( 
       string _filePath_ ,
       [RelativeToDirectory](topic2359.md) _relativePathBehavior_
    )  
  
#### Parameters

 _filePath_
    The file path to resolve, e.g. "<Project>\SomeFile.txt"
_relativePathBehavior_
    The behavior of the resolution if the file path specified is relative rather than qualified with a standard prefix.

#### Return Value

The resolved file path.

# Remarks

The following prefixes are understood by this method:

  * <Project>
  * <Specification>
  * <SpecificationMetadata>
  * <GroupContent>



# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectUtility Class](topic4899.md)   
[ProjectUtility Members](topic4900.md)


